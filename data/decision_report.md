# Decision Report

- generated_at: 2026-08-20T14:16:23.673204+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12050**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12050, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -1.14% | **-0.40%** |
| LIMIT_ATR | 11/20 | 55.0% | -1.23% | **-0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.49% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.12% | **+0.89%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.03% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$602.65** / 初期 $100.00 (+502.65%)
- 確定: 4263件 (Win 1305 / Loss 1393 / Flat 1565) / skip 4348件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $602.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3640件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.69** / 初期 $100.00 (+16.69%)
- 確定: 1757件 (Win 521 / Loss 672 / Flat 564) / pending 0件 / skip 1766件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000044 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUMPFUN/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $116.69

## 6. Latest Market Context

- 更新: 2026-08-20T14:16:14.829624+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=71683.3
- Funnel: target 1011 → liquid 199 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +57.28% | $5,268,628.53 |
| BOME/USDT:USDT | +45.57% | $15,198,657.63 |
| ONG/USDT:USDT | +33.19% | $2,400,253.07 |
| NEIROCTO/USDT:USDT | +30.16% | $1,589,235.36 |
| MAGMA/USDT:USDT | +28.92% | $10,614,651.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +3.40% | +3.36% |
| WIF/USDT:USDT | below_1h_threshold | +2.11% | +2.07% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.23% | +1.19% |
| XRP/USDT:USDT | below_1h_threshold | +1.18% | +1.14% |
| BASECAT/USDT:USDT | below_1h_threshold | +0.95% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
