# Decision Report

- generated_at: 2026-08-14T16:26:32.284822+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11575**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11575, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.12% | **+0.78%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.84% | **+0.67%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.58% | **+0.53%** |
| LIMIT_BB3S | 2/17 | 11.8% | +2.61% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.58% | **+1.43%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.12% | **+1.09%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$634.02** / 初期 $100.00 (+534.02%)
- 確定: 4043件 (Win 1270 / Loss 1330 / Flat 1443) / skip 4093件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.76% 残高後 $634.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3335件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.85** / 初期 $100.00 (+17.85%)
- 確定: 1533件 (Win 467 / Loss 585 / Flat 481) / pending 6件 / skip 1511件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000227 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.85

## 6. Latest Market Context

- 更新: 2026-08-14T16:26:19.587547+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=63073.6
- Funnel: target 985 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +9.77% | $48,770,700.19 |
| US/USDT:USDT | +7.41% | $5,152,955.32 |
| MANA/USDT:USDT | +2.84% | $1,455,779.60 |
| NBISSTOCK/USDT:USDT | +1.96% | $9,731,995.93 |
| GPS/USDT:USDT | +1.82% | $1,100,956.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MANA/USDT:USDT | below_1h_threshold | +2.86% | +2.68% |
| GPS/USDT:USDT | below_1h_threshold | +1.82% | +1.64% |
| BSV/USDT:USDT | below_1h_threshold | +1.72% | +1.54% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.27% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.22% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
