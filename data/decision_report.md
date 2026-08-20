# Decision Report

- generated_at: 2026-08-20T13:41:39.993960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12047**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12047, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.22% | **+0.11%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_3PCT | 12/20 | 60.0% | -0.11% | **-0.07%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.59% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.85% | **+0.74%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.94% | **+0.68%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.51% | **+0.68%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.59% | **+0.56%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.74% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$602.65** / 初期 $100.00 (+502.65%)
- 確定: 4260件 (Win 1305 / Loss 1393 / Flat 1562) / skip 4348件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $602.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3637件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.69** / 初期 $100.00 (+16.69%)
- 確定: 1757件 (Win 521 / Loss 672 / Flat 564) / pending 0件 / skip 1764件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000034 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUMPFUN/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $116.69

## 6. Latest Market Context

- 更新: 2026-08-20T13:41:24.671760+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.82% price=71340.2
- Funnel: target 1011 → liquid 200 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +50.47% | $5,221,833.88 |
| BOME/USDT:USDT | +49.21% | $14,167,006.83 |
| MAGMA/USDT:USDT | +28.19% | $10,448,240.21 |
| NEIROCTO/USDT:USDT | +25.85% | $1,351,231.05 |
| ACE/USDT:USDT | +25.13% | $18,385,179.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +4.83% | +5.65% |
| ROBO/USDT:USDT | below_1h_threshold | +2.79% | +3.61% |
| GALA/USDT:USDT | below_1h_threshold | +1.86% | +2.68% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.66% | +2.48% |
| ON/USDT:USDT | below_1h_threshold | +1.18% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
