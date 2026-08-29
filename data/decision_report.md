# Decision Report

- generated_at: 2026-08-29T06:11:28.867590+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12904**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.31% / filled 20/20。**
- 全期間 MARKET基準: n=12904, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.10% | **+1.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.26% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.39% | **+0.22%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.05% | **+0.02%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$715.98** / 初期 $100.00 (+615.98%)
- 確定: 4678件 (Win 1415 / Loss 1534 / Flat 1729) / skip 4787件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TOAD/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $715.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4312件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.95** / 初期 $100.00 (+15.95%)
- 確定: 2000件 (Win 586 / Loss 768 / Flat 646) / pending 5件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000403 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TOAD/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.95

## 6. Latest Market Context

- 更新: 2026-08-29T06:11:14.062396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=77528.1
- Funnel: target 1023 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +74.40% | $1,131,799.03 |
| BEAT/USDT:USDT | +18.67% | $11,200,597.70 |
| MAGMA/USDT:USDT | +13.98% | $11,929,341.61 |
| SKR/USDT:USDT | +13.42% | $1,560,036.69 |
| DEXE/USDT:USDT | +12.48% | $8,051,143.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.92% | +3.02% |
| SKR/USDT:USDT | below_1h_threshold | +2.67% | +2.77% |
| NIL/USDT:USDT | below_1h_threshold | +1.87% | +1.97% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.77% | +1.87% |
| DEXE/USDT:USDT | below_1h_threshold | +1.27% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
