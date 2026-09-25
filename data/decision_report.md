# Decision Report

- generated_at: 2026-09-25T22:41:29.852842+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15545**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15545, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.72% | **-1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.45% | **-0.09%** |
| LIMIT_BB3S | 6/14 | 42.9% | -0.85% | **-0.36%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.49% | **-0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.06% | **+2.14%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.12% | **+1.59%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.62% | **+1.57%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.33% | **+1.50%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.59% | **+1.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,204.52** / 初期 $100.00 (+1104.52%)
- 確定: 5909件 (Win 1743 / Loss 1894 / Flat 2272) / skip 6197件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,204.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.50** / 初期 $100.00 (+156.50%)
- 確定: 3478件 (Win 953 / Loss 793 / Flat 1732) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0317 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.80** / 初期 $100.00 (+19.80%)
- 確定: 3175件 (Win 934 / Loss 1257 / Flat 984) / pending 4件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.80

## 6. Latest Market Context

- 更新: 2026-09-25T22:41:14.393963+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=84055.6
- Funnel: target 1067 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +39.35% | $1,074,310.63 |
| PHA/USDT:USDT | +25.89% | $22,000,647.89 |
| BR/USDT:USDT | +17.17% | $9,249,558.82 |
| SEI/USDT:USDT | +11.59% | $33,466,976.52 |
| SUI/USDT:USDT | +8.08% | $267,973,788.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +4.26% | +3.89% |
| LTC/USDT:USDT | below_1h_threshold | +3.80% | +3.43% |
| PENGU/USDT:USDT | below_1h_threshold | +3.76% | +3.39% |
| ONDO/USDT:USDT | below_1h_threshold | +3.60% | +3.23% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +3.27% | +2.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
