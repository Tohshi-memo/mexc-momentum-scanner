# Decision Report

- generated_at: 2026-08-25T00:56:28.084070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12560**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12560, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.41% | **+0.72%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.48% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.54% | **+2.30%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.36% | **+1.89%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.71% | **+1.76%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.88% | **+1.30%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.27% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$701.65** / 初期 $100.00 (+601.65%)
- 確定: 4540件 (Win 1384 / Loss 1488 / Flat 1668) / skip 4581件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INJ/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $701.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3998件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0543 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1913件 (Win 561 / Loss 728 / Flat 624) / pending 0件 / skip 2121件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-25T00:56:18.538212+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.04% price=79771.7
- Funnel: target 1022 → liquid 185 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1, 4h RSI 85.7 >= 65=1, 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +106.24% | $3,803,851.03 |
| TAC/USDT:USDT | +34.31% | $1,283,089.65 |
| CASHCAT/USDT:USDT | +24.28% | $2,559,856.36 |
| STORJ/USDT:USDT | +21.38% | $5,310,426.01 |
| ONG/USDT:USDT | +16.21% | $3,227,389.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_relative_strength | +5.64% | +4.61% |
| JUP/USDT:USDT | below_relative_strength | +5.17% | +4.13% |
| ONG/USDT:USDT | below_1h_threshold | +4.70% | +3.67% |
| PROM/USDT:USDT | below_1h_threshold | +4.10% | +3.07% |
| 1000BONK/USDT:USDT | below_1h_threshold | +3.24% | +2.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
