# Decision Report

- generated_at: 2026-11-20T11:56:26.803414+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19241**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=19241, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.99% | **+0.40%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.48% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.22% | **+0.17%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.10% | **+0.10%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.10% | **+0.04%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,701.33** / 初期 $100.00 (+1601.33%)
- 確定: 7388件 (Win 2123 / Loss 2379 / Flat 2886) / skip 8414件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,701.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$440.57** / 初期 $100.00 (+340.57%)
- 確定: 5065件 (Win 1352 / Loss 1087 / Flat 2626) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0027 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $440.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7402件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T11:56:10.968418+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=61782.2
- Funnel: target 1084 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYBER/USDT:USDT | +24.90% | $1,714,880.85 |
| BLESS/USDT:USDT | +22.88% | $16,200,412.87 |
| SOXS/USDT:USDT | +22.22% | $64,566,172.38 |
| EVAA/USDT:USDT | +16.00% | $27,067,689.71 |
| UVXY/USDT:USDT | +14.50% | $4,171,610.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +1.90% | +2.30% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.57% |
| USOIL/USDT:USDT | below_1h_threshold | +0.89% | +1.28% |
| EVAA/USDT:USDT | below_1h_threshold | +0.78% | +1.17% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.68% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
