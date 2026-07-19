# Decision Report

- generated_at: 2026-07-19T08:41:22.418397+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9014**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9014, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.08% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.98% | **+0.25%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.31% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.07% | **+2.46%** |
| MARKET_LONG | 20/20 | 100.0% | +2.13% | **+2.13%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.10% | **+0.95%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.23% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.77** / 初期 $100.00 (+298.77%)
- 確定: 3076件 (Win 963 / Loss 977 / Flat 1136) / skip 2499件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $398.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.99** / 初期 $100.00 (+26.99%)
- 確定: 975件 (Win 249 / Loss 197 / Flat 529) / skip 1450件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2477 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $126.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.51** / 初期 $100.00 (+0.51%)
- 確定: 217件 (Win 69 / Loss 109 / Flat 39) / pending 6件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000553 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.51

## 6. Latest Market Context

- 更新: 2026-07-19T08:41:12.551178+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64627.7
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1, 4h RSI 73.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +132.63% | $43,795,017.09 |
| BANK/USDT:USDT | +65.69% | $19,096,575.90 |
| TLM/USDT:USDT | +52.03% | $5,523,822.65 |
| B/USDT:USDT | +38.79% | $40,359,057.79 |
| BULLA/USDT:USDT | +25.26% | $1,299,245.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.13% | +4.23% |
| BULLA/USDT:USDT | below_1h_threshold | +3.70% | +3.80% |
| PI/USDT:USDT | below_1h_threshold | +3.24% | +3.33% |
| ALLO/USDT:USDT | below_1h_threshold | +2.87% | +2.97% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.82% | +2.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
