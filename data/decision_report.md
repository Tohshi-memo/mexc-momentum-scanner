# Decision Report

- generated_at: 2026-08-23T03:31:27.123358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12438**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12438, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.67% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_BB3S | 6/20 | 30.0% | +0.89% | **+0.27%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.05% | **+1.44%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.68% | **+1.18%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.55% | **+0.93%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.64% | **+0.29%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.33% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$709.67** / 初期 $100.00 (+609.67%)
- 確定: 4465件 (Win 1367 / Loss 1459 / Flat 1639) / skip 4534件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $709.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3914件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2048件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000138 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T03:31:15.780102+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=76989.6
- Funnel: target 1018 → liquid 207 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.3 >= 65=1, 4h RSI 80.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +57.22% | $47,518,708.72 |
| ZRO/USDT:USDT | +12.68% | $10,953,323.78 |
| TST/USDT:USDT | +11.74% | $1,024,643.35 |
| UAI/USDT:USDT | +10.73% | $3,340,857.17 |
| SQD/USDT:USDT | +7.99% | $2,661,361.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +2.64% | +2.76% |
| SYN/USDT:USDT | below_1h_threshold | +2.36% | +2.48% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +2.08% |
| ONG/USDT:USDT | below_1h_threshold | +0.74% | +0.86% |
| BR/USDT:USDT | below_1h_threshold | +0.62% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
