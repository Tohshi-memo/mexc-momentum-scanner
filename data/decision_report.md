# Decision Report

- generated_at: 2026-07-22T20:51:27.746019+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9321**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9321, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.28% | **+0.39%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.63% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.22% | **+2.90%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.39% | **+2.39%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.98% | **+1.29%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.24% | **+1.23%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$105.37** / 初期 $100.00 (+5.37%)
- 確定トレード: 133件 (TP 45 / SL 83 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$436.91** / 初期 $100.00 (+336.91%)
- 確定: 3306件 (Win 1044 / Loss 1065 / Flat 1197) / skip 2576件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $436.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1571件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1144 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.37** / 初期 $100.00 (+1.37%)
- 確定: 426件 (Win 142 / Loss 177 / Flat 107) / pending 2件 / skip 372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000330 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.37

## 6. Latest Market Context

- 更新: 2026-07-22T20:51:19.087438+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=65886.2
- Funnel: target 890 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +54.26% | $4,358,491.64 |
| BANK/USDT:USDT | +19.97% | $105,101,470.54 |
| BROCCOLIF3B/USDT:USDT | +17.74% | $1,738,333.64 |
| RIF/USDT:USDT | +11.75% | $4,036,350.95 |
| ON/USDT:USDT | +9.29% | $1,715,689.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BROCCOLIF3B/USDT:USDT | below_1h_threshold | +4.13% | +4.14% |
| ZAMA/USDT:USDT | below_1h_threshold | +3.40% | +3.41% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.78% | +2.79% |
| EVAA/USDT:USDT | below_1h_threshold | +2.53% | +2.54% |
| DODO/USDT:USDT | below_1h_threshold | +1.85% | +1.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
