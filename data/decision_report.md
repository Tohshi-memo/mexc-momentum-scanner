# Decision Report

- generated_at: 2026-09-04T01:51:43.018432+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13567**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=13567, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.34% | **+1.20%** |
| LIMIT_BB3S | 4/19 | 21.1% | +4.67% | **+0.98%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.76% | **+0.45%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.66% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.14% | **+0.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5119件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.25** / 初期 $100.00 (+85.25%)
- 確定: 2384件 (Win 676 / Loss 576 / Flat 1132) / skip 4594件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0642 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.02** / 初期 $100.00 (+17.02%)
- 確定: 2224件 (Win 663 / Loss 871 / Flat 690) / pending 6件 / skip 2813件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.02

## 6. Latest Market Context

- 更新: 2026-09-04T01:51:27.113813+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=80836.3
- Funnel: target 1046 → liquid 169 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1, 4h RSI 75.2 >= 65=1, 4h RSI 89.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +34.52% | $9,798,587.68 |
| BASECAT/USDT:USDT | +25.54% | $1,943,589.72 |
| PONS/USDT:USDT | +17.09% | $9,675,049.63 |
| MARSCOIN/USDT:USDT | +14.24% | $9,951,015.65 |
| USELESS/USDT:USDT | +13.62% | $28,314,839.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.39% | +4.51% |
| BR/USDT:USDT | below_1h_threshold | +4.21% | +4.33% |
| BTR/USDT:USDT | below_1h_threshold | +2.85% | +2.98% |
| CHIP/USDT:USDT | below_1h_threshold | +2.65% | +2.77% |
| ZRO/USDT:USDT | below_1h_threshold | +1.93% | +2.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
