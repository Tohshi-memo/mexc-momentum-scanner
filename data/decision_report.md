# Decision Report

- generated_at: 2026-07-21T01:36:22.808520+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9136**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9136, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.54% | **+1.31%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.79% | **+0.75%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.11% | **+0.08%** |
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.93% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$402.41** / 初期 $100.00 (+302.41%)
- 確定: 3198件 (Win 1000 / Loss 1017 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $402.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.30** / 初期 $100.00 (+27.30%)
- 確定: 1097件 (Win 286 / Loss 225 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000220 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1145 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $127.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定: 333件 (Win 118 / Loss 146 / Flat 69) / pending 5件 / skip 272件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.63

## 6. Latest Market Context

- 更新: 2026-07-21T01:36:13.866453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=65419.8
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +40.28% | $2,738,438.24 |
| HEMI/USDT:USDT | +16.52% | $3,079,210.85 |
| BLESS/USDT:USDT | +11.67% | $1,597,092.08 |
| LDO/USDT:USDT | +9.56% | $6,023,784.07 |
| ESPORTS/USDT:USDT | +9.27% | $7,196,287.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.25% | +3.44% |
| ON/USDT:USDT | below_1h_threshold | +2.48% | +2.67% |
| BLESS/USDT:USDT | below_1h_threshold | +2.32% | +2.51% |
| SLX/USDT:USDT | below_1h_threshold | +1.06% | +1.25% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.01% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
