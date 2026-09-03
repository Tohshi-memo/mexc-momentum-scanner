# Decision Report

- generated_at: 2026-09-03T14:31:48.725925+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13481**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13481, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.70% | **-2.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +1.15% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.10% | **+2.17%** |
| MARKET_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.89% | **+1.75%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.12% | **+1.72%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.26% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5034件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4519件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1836 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.82** / 初期 $100.00 (+16.82%)
- 確定: 2174件 (Win 648 / Loss 850 / Flat 676) / pending 6件 / skip 2778件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000461 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRCLSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.16% 残高後 $116.82

## 6. Latest Market Context

- 更新: 2026-09-03T14:31:29.550107+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.19% price=79747.3
- Funnel: target 1046 → liquid 161 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.4 >= 65=1, 4h RSI 84.6 >= 65=1, 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +96.01% | $8,915,412.49 |
| BASECAT/USDT:USDT | +64.25% | $1,105,165.16 |
| BR/USDT:USDT | +54.07% | $5,727,712.21 |
| BULLA/USDT:USDT | +49.84% | $8,628,576.51 |
| EDGE/USDT:USDT | +45.61% | $7,523,705.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.62% | +3.43% |
| CATI/USDT:USDT | below_1h_threshold | +4.20% | +3.01% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +3.80% | +2.60% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +3.48% | +2.29% |
| SOXS/USDT:USDT | below_1h_threshold | +3.01% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
