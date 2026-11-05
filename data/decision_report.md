# Decision Report

- generated_at: 2026-11-05T01:51:13.474281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18149**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=18149, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.91% | **+0.68%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.74% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.40% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,500.99** / 初期 $100.00 (+1400.99%)
- 確定: 6968件 (Win 2016 / Loss 2238 / Flat 2714) / skip 7742件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.28% 残高後 $1,500.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$373.32** / 初期 $100.00 (+273.32%)
- 確定: 4556件 (Win 1223 / Loss 1029 / Flat 2304) / skip 7004件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MRNASTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $373.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6307件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000019 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T01:51:05.070134+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=80728.4
- Funnel: target 1078 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELSA/USDT:USDT | +29.05% | $2,209,455.52 |
| APPSTOCK/USDT:USDT | +21.01% | $1,300,999.11 |
| FLUID/USDT:USDT | +14.62% | $3,959,247.91 |
| LSK/USDT:USDT | +8.43% | $7,097,830.41 |
| ICNT/USDT:USDT | +7.61% | $1,137,036.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +3.53% | +3.26% |
| AXIS/USDT:USDT | below_1h_threshold | +2.13% | +1.86% |
| RUNE/USDT:USDT | below_1h_threshold | +2.12% | +1.84% |
| JCT/USDT:USDT | below_1h_threshold | +1.97% | +1.70% |
| NIL/USDT:USDT | below_1h_threshold | +1.88% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
