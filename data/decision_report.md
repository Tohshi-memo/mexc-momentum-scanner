# Decision Report

- generated_at: 2026-09-16T11:56:55.724487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14682**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14682, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.40% | **-2.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.48% | **+1.12%** |
| LIMIT_9PCT | 6/20 | 30.0% | +3.43% | **+1.03%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.75% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.28% | **+3.12%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.03% | **+2.42%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +4.01% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,116.74** / 初期 $100.00 (+1016.74%)
- 確定: 5559件 (Win 1661 / Loss 1796 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,116.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$233.21** / 初期 $100.00 (+133.21%)
- 確定: 3087件 (Win 850 / Loss 728 / Flat 1509) / skip 5006件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0013 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $233.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3202件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000115 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T11:56:33.134830+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=76208.5
- Funnel: target 1058 → liquid 153 → pre 50 → checked 50 → surge 6 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.7 >= 65=1, 4h RSI 66.3 >= 65=1, 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +129.77% | $19,173,648.91 |
| BR/USDT:USDT | +102.98% | $23,654,819.34 |
| LSK/USDT:USDT | +63.40% | $25,877,745.68 |
| BULLA/USDT:USDT | +55.62% | $1,642,843.78 |
| USELESS/USDT:USDT | +15.81% | $7,781,283.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +3.79% | +3.42% |
| ARB/USDT:USDT | below_1h_threshold | +3.45% | +3.09% |
| ON/USDT:USDT | below_1h_threshold | +3.41% | +3.05% |
| VVV/USDT:USDT | below_1h_threshold | +2.73% | +2.37% |
| SPX/USDT:USDT | below_1h_threshold | +2.54% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
