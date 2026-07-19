# Decision Report

- generated_at: 2026-07-19T12:31:23.770873+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9035**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9035, expectancy=-0.01%
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
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.39% | **+0.72%** |
| LIMIT_2PCT | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.58% | **+1.55%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$404.36** / 初期 $100.00 (+304.36%)
- 確定: 3097件 (Win 971 / Loss 985 / Flat 1141) / skip 2499件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $404.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$128.11** / 初期 $100.00 (+28.11%)
- 確定: 996件 (Win 257 / Loss 205 / Flat 534) / skip 1450件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1677 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $128.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.06** / 初期 $100.00 (+1.06%)
- 確定: 236件 (Win 79 / Loss 117 / Flat 40) / pending 4件 / skip 266件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000509 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.06

## 6. Latest Market Context

- 更新: 2026-07-19T12:31:13.226145+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=64317.6
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +115.38% | $34,404,291.24 |
| ESPORTS/USDT:USDT | +92.62% | $54,017,143.26 |
| TLM/USDT:USDT | +80.28% | $7,517,936.68 |
| B/USDT:USDT | +58.02% | $37,991,140.23 |
| TAG/USDT:USDT | +25.28% | $4,655,165.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +4.30% | +4.50% |
| XLM/USDT:USDT | below_1h_threshold | +1.40% | +1.60% |
| BLESS/USDT:USDT | below_1h_threshold | +1.02% | +1.22% |
| ORDI/USDT:USDT | below_1h_threshold | +0.88% | +1.08% |
| PEPE/USDT:USDT | below_1h_threshold | +0.64% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
