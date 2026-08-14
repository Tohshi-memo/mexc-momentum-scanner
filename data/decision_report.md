# Decision Report

- generated_at: 2026-08-14T16:21:29.319327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11574**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11574, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.78% | **+0.58%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.65% | **+0.52%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.94% | **+1.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.22% | **+1.13%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.12% | **+1.09%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.49% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$629.21** / 初期 $100.00 (+529.21%)
- 確定: 4042件 (Win 1269 / Loss 1330 / Flat 1443) / skip 4093件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $629.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3334件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0173 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.85** / 初期 $100.00 (+17.85%)
- 確定: 1533件 (Win 467 / Loss 585 / Flat 481) / pending 6件 / skip 1510件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000229 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.85

## 6. Latest Market Context

- 更新: 2026-08-14T16:21:16.817247+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=63021.3
- Funnel: target 985 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +8.90% | $48,278,475.95 |
| US/USDT:USDT | +6.73% | $5,047,759.60 |
| CAP/USDT:USDT | +4.07% | $9,216,942.07 |
| AKE/USDT:USDT | +2.98% | $66,816,337.90 |
| MANA/USDT:USDT | +2.80% | $1,447,059.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +3.72% | +3.61% |
| AKE/USDT:USDT | below_1h_threshold | +3.14% | +3.04% |
| MANA/USDT:USDT | below_1h_threshold | +2.79% | +2.68% |
| CROSS/USDT:USDT | below_1h_threshold | +1.74% | +1.64% |
| BSV/USDT:USDT | below_1h_threshold | +1.59% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
