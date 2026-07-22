# Decision Report

- generated_at: 2026-07-22T01:46:19.211776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9231, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.12% | **-1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.71% | **+1.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.33% | **+0.73%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.88% | **+2.52%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.34% | **+1.27%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.67% | **+1.25%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.96% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2542件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1483件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.17** / 初期 $100.00 (+1.17%)
- 確定: 376件 (Win 125 / Loss 156 / Flat 95) / pending 4件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000070 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.17% 残高後 $101.17

## 6. Latest Market Context

- 更新: 2026-07-22T01:46:14.545461+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=66337.5
- Funnel: target 885 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +27.16% | $3,967,468.40 |
| PONS/USDT:USDT | +25.42% | $2,083,215.94 |
| SMCISTOCK/USDT:USDT | +19.62% | $3,525,951.33 |
| FWDISTOCK/USDT:USDT | +13.59% | $3,944,883.68 |
| RE/USDT:USDT | +11.61% | $1,483,096.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANTHROPIC/USDT:USDT | below_1h_threshold | +3.75% | +4.13% |
| TLM/USDT:USDT | below_1h_threshold | +2.57% | +2.96% |
| LAB/USDT:USDT | below_1h_threshold | +2.40% | +2.78% |
| OPENAI/USDT:USDT | below_1h_threshold | +1.69% | +2.07% |
| US/USDT:USDT | below_1h_threshold | +1.68% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
