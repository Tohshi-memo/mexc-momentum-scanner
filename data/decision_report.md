# Decision Report

- generated_at: 2026-08-24T11:56:32.787842+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12510**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12510, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.73% | **+1.91%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.61% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.80% | **+1.44%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4510件 (Win 1375 / Loss 1477 / Flat 1658) / skip 4561件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1969件 (Win 536 / Loss 470 / Flat 963) / skip 3952件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0123 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.23** / 初期 $100.00 (+16.23%)
- 確定: 1893件 (Win 557 / Loss 717 / Flat 619) / pending 6件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000070 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.23

## 6. Latest Market Context

- 更新: 2026-08-24T11:56:20.695253+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.70% price=78158.1
- Funnel: target 1019 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +54.94% | $1,313,511.43 |
| PROM/USDT:USDT | +38.52% | $11,451,456.56 |
| PORTAL/USDT:USDT | +31.91% | $3,511,046.27 |
| CASHCAT/USDT:USDT | +28.58% | $1,130,155.73 |
| UAI/USDT:USDT | +23.66% | $12,837,120.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +4.90% | +4.20% |
| CYS/USDT:USDT | below_1h_threshold | +3.49% | +2.79% |
| FET/USDT:USDT | below_1h_threshold | +3.35% | +2.65% |
| AERO/USDT:USDT | below_1h_threshold | +3.30% | +2.60% |
| MORPHO/USDT:USDT | below_1h_threshold | +3.00% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
