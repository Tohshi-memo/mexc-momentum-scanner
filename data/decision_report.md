# Decision Report

- generated_at: 2026-07-22T17:36:31.971042+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9299**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9299, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/17 | 23.5% | +1.25% | **+0.29%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.45% | **+0.29%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.34% | **+0.20%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.44% | **+0.87%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.18% | **+0.65%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.78% | **+0.55%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.87% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$105.37** / 初期 $100.00 (+5.37%)
- 確定トレード: 133件 (TP 45 / SL 83 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$431.91** / 初期 $100.00 (+331.91%)
- 確定: 3289件 (Win 1039 / Loss 1058 / Flat 1192) / skip 2571件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $431.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1550件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0695 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 425件 (Win 142 / Loss 176 / Flat 107) / pending 3件 / skip 353件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.55

## 6. Latest Market Context

- 更新: 2026-07-22T17:36:22.777579+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=66057.4
- Funnel: target 890 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +11.10% | $92,800,082.84 |
| WLD/USDT:USDT | +5.61% | $34,244,569.70 |
| JIMOTHY/USDT:USDT | +5.43% | $3,272,149.95 |
| BROCCOLIF3B/USDT:USDT | +5.25% | $1,575,592.55 |
| DEXE/USDT:USDT | +4.03% | $13,976,817.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +3.81% | +4.03% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.19% | +2.40% |
| WLD/USDT:USDT | below_1h_threshold | +2.16% | +2.37% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.74% | +1.96% |
| UB/USDT:USDT | below_1h_threshold | +1.69% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
