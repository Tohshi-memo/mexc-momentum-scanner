# Decision Report

- generated_at: 2026-08-24T16:21:39.462800+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12523**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12523, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.25% | **+0.50%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.57% | **+0.43%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.00% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.54% | **+1.39%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.61% | **+1.05%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.27% | **+0.57%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.79% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4510件 (Win 1375 / Loss 1477 / Flat 1658) / skip 4574件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1972件 (Win 536 / Loss 470 / Flat 966) / skip 3962件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.45** / 初期 $100.00 (+15.45%)
- 確定: 1906件 (Win 559 / Loss 723 / Flat 624) / pending 6件 / skip 2085件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.45

## 6. Latest Market Context

- 更新: 2026-08-24T16:21:25.339413+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.75% price=79662.0
- Funnel: target 1022 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +7.37% | $1,854,344.84 |
| US/USDT:USDT | +7.23% | $1,905,353.37 |
| CASHCAT/USDT:USDT | +6.18% | $1,745,337.62 |
| AERO/USDT:USDT | +4.21% | $2,138,108.19 |
| LUNC/USDT:USDT | +2.94% | $1,425,325.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.93% | +3.18% |
| AERO/USDT:USDT | below_1h_threshold | +3.92% | +3.17% |
| TURBO/USDT:USDT | below_1h_threshold | +2.77% | +2.02% |
| LUNC/USDT:USDT | below_1h_threshold | +2.51% | +1.75% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.07% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
