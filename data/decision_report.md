# Decision Report

- generated_at: 2026-07-30T04:36:15.174368+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9860**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.93% / filled 20/20。**
- 全期間 MARKET基準: n=9860, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.05% | **+2.44%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.49% | **+1.49%** |
| LIMIT_BB3S | 4/16 | 25.0% | +4.14% | **+1.03%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.74% | **+0.96%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.62% | **-0.34%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -1.12% | **-0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 170件 (TP 67 / SL 98 / EXP 5)
- 最新: LASERTECSTOCK/USDT:USDT TP_HIT PnL +3.98% 残高後 $121.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2902件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2029件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.51** / 初期 $100.00 (+10.51%)
- 確定: 773件 (Win 251 / Loss 299 / Flat 223) / pending 0件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000791 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.51

## 6. Latest Market Context

- 更新: 2026-07-30T04:36:09.675119+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64108.8
- Funnel: target 911 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +17.82% | $1,291,519.40 |
| RE/USDT:USDT | +15.45% | $8,740,803.96 |
| MMT/USDT:USDT | +14.91% | $1,032,073.02 |
| UAI/USDT:USDT | +13.77% | $16,624,078.88 |
| MSFU/USDT:USDT | +13.56% | $3,891,859.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.94% | +4.98% |
| HOLO/USDT:USDT | below_1h_threshold | +2.82% | +2.86% |
| QXOSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +2.00% |
| RE/USDT:USDT | below_1h_threshold | +1.41% | +1.45% |
| CAP/USDT:USDT | below_1h_threshold | +1.28% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
