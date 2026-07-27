# Decision Report

- generated_at: 2026-07-27T06:36:35.820880+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9605**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9605, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 19/20 | 95.0% | +1.38% | **+1.31%** |
| LIMIT_10PCT | 5/20 | 25.0% | +5.09% | **+1.27%** |
| LIMIT_9PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.22% | **+0.21%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +2.32% | **+1.80%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.34% | **+1.64%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.87% | **+1.50%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.85% | **+1.48%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.58% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.80** / 初期 $100.00 (+354.80%)
- 確定: 3402件 (Win 1079 / Loss 1107 / Flat 1216) / skip 2764件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $454.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1793件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.09** / 初期 $100.00 (+8.09%)
- 確定: 631件 (Win 210 / Loss 241 / Flat 180) / pending 5件 / skip 442件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000038 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.09

## 6. Latest Market Context

- 更新: 2026-07-27T06:36:22.557518+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=65523.6
- Funnel: target 903 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1, 4h RSI 79.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +68.48% | $27,679,323.09 |
| BANK/USDT:USDT | +41.47% | $76,662,334.23 |
| DIA/USDT:USDT | +24.37% | $7,873,313.14 |
| ON/USDT:USDT | +23.43% | $3,790,631.59 |
| BTW/USDT:USDT | +23.30% | $1,458,461.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DIA/USDT:USDT | below_1h_threshold | +4.74% | +4.60% |
| LDO/USDT:USDT | below_1h_threshold | +3.07% | +2.93% |
| B/USDT:USDT | below_1h_threshold | +2.07% | +1.93% |
| NIL/USDT:USDT | below_1h_threshold | +1.88% | +1.74% |
| BTW/USDT:USDT | below_1h_threshold | +1.46% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
