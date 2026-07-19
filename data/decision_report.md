# Decision Report

- generated_at: 2026-07-19T12:56:24.697053+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9037**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9037, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +2.75% | **+1.24%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.38% | **+1.09%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.81% | **+0.64%** |
| LIMIT_2PCT | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.58% | **+1.55%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.41% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$402.33** / 初期 $100.00 (+302.33%)
- 確定: 3099件 (Win 971 / Loss 986 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $402.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.66** / 初期 $100.00 (+27.66%)
- 確定: 998件 (Win 257 / Loss 206 / Flat 535) / skip 1450件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1561 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $127.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.05** / 初期 $100.00 (+1.05%)
- 確定: 238件 (Win 80 / Loss 118 / Flat 40) / pending 4件 / skip 266件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000504 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.05

## 6. Latest Market Context

- 更新: 2026-07-19T12:56:15.531741+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64406.0
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +122.53% | $36,398,413.45 |
| ESPORTS/USDT:USDT | +90.32% | $54,772,865.25 |
| TLM/USDT:USDT | +82.02% | $7,816,193.31 |
| B/USDT:USDT | +56.32% | $38,532,885.75 |
| TAG/USDT:USDT | +27.79% | $4,717,444.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.91% | +4.98% |
| B/USDT:USDT | below_1h_threshold | +3.36% | +3.43% |
| AKE/USDT:USDT | below_1h_threshold | +2.44% | +2.50% |
| LYN/USDT:USDT | below_1h_threshold | +1.66% | +1.72% |
| XLM/USDT:USDT | below_1h_threshold | +1.18% | +1.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
