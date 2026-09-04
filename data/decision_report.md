# Decision Report

- generated_at: 2026-09-04T04:46:45.714952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13580**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=13580, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.25% | **+0.88%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_BB3S | 2/18 | 11.1% | +5.22% | **+0.58%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.22% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.35% | **-0.28%** |
| MARKET_LONG | 20/20 | 100.0% | -0.32% | **-0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5132件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.64** / 初期 $100.00 (+85.64%)
- 確定: 2396件 (Win 679 / Loss 576 / Flat 1141) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0655 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.55** / 初期 $100.00 (+16.55%)
- 確定: 2234件 (Win 665 / Loss 875 / Flat 694) / pending 6件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.55

## 6. Latest Market Context

- 更新: 2026-09-04T04:46:32.589373+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=81022.4
- Funnel: target 1046 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +29.64% | $11,658,362.34 |
| BASECAT/USDT:USDT | +22.52% | $2,121,876.78 |
| USELESS/USDT:USDT | +18.41% | $30,119,950.70 |
| TRIA/USDT:USDT | +16.14% | $2,440,995.29 |
| PROM/USDT:USDT | +14.13% | $2,883,352.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_relative_strength | +5.09% | +4.83% |
| BTR/USDT:USDT | below_1h_threshold | +4.19% | +3.93% |
| BASECAT/USDT:USDT | below_1h_threshold | +3.64% | +3.37% |
| PROM/USDT:USDT | below_1h_threshold | +2.56% | +2.29% |
| XPL/USDT:USDT | below_1h_threshold | +2.12% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
