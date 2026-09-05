# Decision Report

- generated_at: 2026-09-05T18:21:17.659435+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13769**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13769, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.50% | **+0.35%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.71% | **+0.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.56% | **+0.25%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.19% | **+0.08%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.01** / 初期 $100.00 (+759.01%)
- 確定: 5075件 (Win 1522 / Loss 1654 / Flat 1899) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $859.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.32** / 初期 $100.00 (+88.32%)
- 確定: 2514件 (Win 700 / Loss 593 / Flat 1221) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0546 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.74** / 初期 $100.00 (+19.74%)
- 確定: 2386件 (Win 708 / Loss 905 / Flat 773) / pending 3件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.74

## 6. Latest Market Context

- 更新: 2026-09-05T18:21:07.555093+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=79982.7
- Funnel: target 1050 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +28.41% | $25,318,689.68 |
| MAGMA/USDT:USDT | +20.86% | $2,259,153.61 |
| USELESS/USDT:USDT | +13.83% | $20,699,790.72 |
| NIULAI/USDT:USDT | +12.10% | $2,739,353.94 |
| BASECAT/USDT:USDT | +11.52% | $2,079,336.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +2.91% | +2.97% |
| ARB/USDT:USDT | below_1h_threshold | +2.59% | +2.65% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.08% | +2.14% |
| CRV/USDT:USDT | below_1h_threshold | +1.83% | +1.89% |
| USELESS/USDT:USDT | below_1h_threshold | +1.57% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
