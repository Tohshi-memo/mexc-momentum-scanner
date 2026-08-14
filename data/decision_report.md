# Decision Report

- generated_at: 2026-08-14T18:11:38.900052+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11590**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11590, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 19/20 | 95.0% | +1.38% | **+1.31%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.86% | **+0.82%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.47% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.18% | **+2.07%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$649.65** / 初期 $100.00 (+549.65%)
- 確定: 4058件 (Win 1275 / Loss 1333 / Flat 1450) / skip 4093件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $649.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.89** / 初期 $100.00 (+52.89%)
- 確定: 1657件 (Win 476 / Loss 399 / Flat 782) / skip 3344件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1066 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $152.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.02** / 初期 $100.00 (+17.02%)
- 確定: 1542件 (Win 468 / Loss 590 / Flat 484) / pending 6件 / skip 1517件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.02

## 6. Latest Market Context

- 更新: 2026-08-14T18:11:22.512461+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63029.0
- Funnel: target 985 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +38.66% | $72,606,548.38 |
| US/USDT:USDT | +23.77% | $6,261,697.48 |
| ACE/USDT:USDT | +14.56% | $55,138,307.59 |
| AVNT/USDT:USDT | +4.40% | $2,739,280.40 |
| ACU/USDT:USDT | +4.19% | $2,498,947.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +2.87% | +2.81% |
| ACE/USDT:USDT | below_1h_threshold | +1.85% | +1.78% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.58% |
| APR/USDT:USDT | below_1h_threshold | +1.26% | +1.20% |
| BTW/USDT:USDT | below_1h_threshold | +1.15% | +1.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
