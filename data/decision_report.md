# Decision Report

- generated_at: 2026-08-23T16:31:26.000517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12460**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12460, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.46% | **+0.25%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_BB3S | 6/15 | 40.0% | -0.13% | **-0.05%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.12% | **-0.08%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.34% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.70% | **+2.70%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.43% | **+1.34%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$700.62** / 初期 $100.00 (+600.62%)
- 確定: 4487件 (Win 1370 / Loss 1470 / Flat 1647) / skip 4534件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $700.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.42** / 初期 $100.00 (+57.42%)
- 確定: 1939件 (Win 534 / Loss 466 / Flat 939) / skip 3932件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PENGU/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $157.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1865件 (Win 550 / Loss 707 / Flat 608) / pending 0件 / skip 2069件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `MARKET` EXPIRED account +0.24% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-23T16:31:16.896566+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=77301.4
- Funnel: target 1018 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +9.53% | $2,693,928.53 |
| ON/USDT:USDT | +4.08% | $1,351,043.89 |
| PENGU/USDT:USDT | +3.91% | $9,633,590.35 |
| STX/USDT:USDT | +3.25% | $13,901,626.51 |
| CHIP/USDT:USDT | +2.78% | $2,338,994.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +4.08% | +3.85% |
| PENGU/USDT:USDT | below_1h_threshold | +3.84% | +3.61% |
| STX/USDT:USDT | below_1h_threshold | +3.25% | +3.02% |
| CHIP/USDT:USDT | below_1h_threshold | +2.78% | +2.55% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.18% | +1.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
