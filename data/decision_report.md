# Decision Report

- generated_at: 2026-09-09T00:51:15.919490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14025**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=14025, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.67% | **+1.26%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.88% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.21% | **-0.11%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | -0.64% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.58** / 初期 $100.00 (+913.58%)
- 確定: 5289件 (Win 1588 / Loss 1707 / Flat 1994) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WAVES/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,013.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.66** / 初期 $100.00 (+90.66%)
- 確定: 2628件 (Win 726 / Loss 622 / Flat 1280) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0470 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: WAVES/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 2607件 (Win 763 / Loss 991 / Flat 853) / pending 4件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000120 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WAVES/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-09-09T00:51:07.218934+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=78736.1
- Funnel: target 1070 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1, 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +34.64% | $1,698,339.76 |
| WAVES/USDT:USDT | +23.51% | $1,194,785.89 |
| EGLD/USDT:USDT | +9.70% | $2,224,901.25 |
| ARX/USDT:USDT | +9.30% | $1,322,301.37 |
| RAY/USDT:USDT | +6.44% | $3,052,195.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.97% | +2.57% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +2.48% |
| KAS/USDT:USDT | below_1h_threshold | +1.97% | +1.58% |
| ETC/USDT:USDT | below_1h_threshold | +1.84% | +1.44% |
| JUP/USDT:USDT | below_1h_threshold | +1.75% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
