# Decision Report

- generated_at: 2026-08-23T04:36:25.162704+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12441**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12441, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.47% | **+0.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +2.05% | **+1.64%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.62% | **+1.13%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.97% | **+0.78%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$709.61** / 初期 $100.00 (+609.61%)
- 確定: 4468件 (Win 1368 / Loss 1461 / Flat 1639) / skip 4534件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGI/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $709.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3917件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0065 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2051件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000110 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T04:36:14.526440+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=76848.0
- Funnel: target 1018 → liquid 207 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +37.68% | $50,205,898.61 |
| ZRO/USDT:USDT | +11.87% | $11,367,941.98 |
| UAI/USDT:USDT | +10.91% | $3,404,862.55 |
| AGI/USDT:USDT | +7.76% | $1,032,029.87 |
| SQD/USDT:USDT | +6.87% | $2,714,390.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +4.72% | +4.84% |
| AGI/USDT:USDT | below_1h_threshold | +3.42% | +3.54% |
| RE/USDT:USDT | below_1h_threshold | +3.13% | +3.25% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.99% | +3.11% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.54% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
