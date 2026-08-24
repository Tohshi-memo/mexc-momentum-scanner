# Decision Report

- generated_at: 2026-08-24T16:36:43.606033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12524**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12524, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.00% | **+0.45%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.54% | **+0.43%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.64% | **+0.41%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.87% | **+1.59%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.08% | **+1.25%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.93% | **+0.77%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.27% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4510件 (Win 1375 / Loss 1477 / Flat 1658) / skip 4575件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1972件 (Win 536 / Loss 470 / Flat 966) / skip 3963件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.25** / 初期 $100.00 (+15.25%)
- 確定: 1907件 (Win 559 / Loss 724 / Flat 624) / pending 6件 / skip 2086件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.25

## 6. Latest Market Context

- 更新: 2026-08-24T16:36:31.328399+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.85% price=79739.3
- Funnel: target 1022 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +11.46% | $2,034,312.86 |
| TUT/USDT:USDT | +6.98% | $60,856,286.18 |
| CASHCAT/USDT:USDT | +6.45% | $1,783,591.54 |
| INJ/USDT:USDT | +4.01% | $14,422,020.71 |
| US/USDT:USDT | +3.99% | $1,954,574.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.04% | +3.19% |
| INJ/USDT:USDT | below_1h_threshold | +3.98% | +3.13% |
| SNXX/USDT:USDT | below_1h_threshold | +3.93% | +3.08% |
| USELESS/USDT:USDT | below_1h_threshold | +3.85% | +3.00% |
| LUNC/USDT:USDT | below_1h_threshold | +3.51% | +2.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
