# Decision Report

- generated_at: 2026-07-22T18:41:32.201678+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9308**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9308, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.30% | **+0.72%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.42% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.29% | **+1.60%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.81% | **+1.09%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.17% | **+1.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.59% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$105.37** / 初期 $100.00 (+5.37%)
- 確定トレード: 133件 (TP 45 / SL 83 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$427.23** / 初期 $100.00 (+327.23%)
- 確定: 3293件 (Win 1039 / Loss 1061 / Flat 1193) / skip 2576件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $427.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1558件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0257 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.37** / 初期 $100.00 (+1.37%)
- 確定: 426件 (Win 142 / Loss 177 / Flat 107) / pending 2件 / skip 358件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.37

## 6. Latest Market Context

- 更新: 2026-07-22T18:41:23.318002+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=65721.6
- Funnel: target 890 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +25.08% | $3,413,363.10 |
| BANK/USDT:USDT | +19.07% | $97,672,554.66 |
| BROCCOLIF3B/USDT:USDT | +10.48% | $1,634,221.66 |
| ON/USDT:USDT | +8.65% | $1,133,246.32 |
| WLD/USDT:USDT | +3.64% | $35,879,724.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +4.64% | +5.06% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.98% | +1.40% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +0.93% | +1.34% |
| BROCCOLIF3B/USDT:USDT | below_1h_threshold | +0.63% | +1.05% |
| USOIL/USDT:USDT | below_1h_threshold | +0.57% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
