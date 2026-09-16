# Decision Report

- generated_at: 2026-09-16T11:51:58.470765+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14681**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14681, expectancy=+0.00%
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
| LIMIT_6PCT | 9/20 | 45.0% | -0.05% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.12% | **+2.97%** |
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.91% | **+2.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.45% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,105.69** / 初期 $100.00 (+1005.69%)
- 確定: 5558件 (Win 1660 / Loss 1796 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,105.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.62** / 初期 $100.00 (+131.62%)
- 確定: 3086件 (Win 849 / Loss 728 / Flat 1509) / skip 5006件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0340 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $231.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000115 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T11:51:41.845166+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=76239.1
- Funnel: target 1058 → liquid 153 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1, 4h RSI 65.9 >= 65=1, 4h RSI 82.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +127.20% | $19,045,290.67 |
| BR/USDT:USDT | +97.15% | $23,150,110.66 |
| LSK/USDT:USDT | +62.35% | $25,655,244.39 |
| BULLA/USDT:USDT | +49.52% | $1,554,647.37 |
| USELESS/USDT:USDT | +16.31% | $7,733,438.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IOST/USDT:USDT | below_relative_strength | +5.08% | +4.68% |
| RAY/USDT:USDT | below_1h_threshold | +4.10% | +3.70% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.12% | +2.72% |
| DASH/USDT:USDT | below_1h_threshold | +3.06% | +2.65% |
| ARB/USDT:USDT | below_1h_threshold | +2.97% | +2.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
