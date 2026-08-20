# Decision Report

- generated_at: 2026-08-20T07:56:31.646737+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12018**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12018, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.35% | **+0.41%** |
| LIMIT_BB3S | 6/14 | 42.9% | +0.81% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_4PCT | 8/20 | 40.0% | +0.54% | **+0.22%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.35% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.55% | **+1.09%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.27% | **+1.06%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.48% | **+1.03%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.92% | **+0.83%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.20** / 初期 $100.00 (+506.20%)
- 確定: 4242件 (Win 1303 / Loss 1388 / Flat 1551) / skip 4337件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BOME/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $606.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3608件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.76** / 初期 $100.00 (+16.76%)
- 確定: 1754件 (Win 520 / Loss 670 / Flat 564) / pending 3件 / skip 1736件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000546 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINIMAXSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.76

## 6. Latest Market Context

- 更新: 2026-08-20T07:56:22.472811+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=69763.6
- Funnel: target 1004 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1, 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BOME/USDT:USDT | +34.13% | $3,033,012.09 |
| BASECAT/USDT:USDT | +28.48% | $1,230,231.61 |
| MAGMA/USDT:USDT | +27.30% | $7,541,323.18 |
| RED/USDT:USDT | +20.96% | $2,095,172.72 |
| LIT/USDT:USDT | +19.67% | $9,748,703.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.48% | +4.59% |
| STAR/USDT:USDT | below_1h_threshold | +4.11% | +4.22% |
| RE/USDT:USDT | below_1h_threshold | +4.02% | +4.13% |
| ASP/USDT:USDT | below_1h_threshold | +2.88% | +2.99% |
| KORU/USDT:USDT | below_1h_threshold | +2.40% | +2.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
