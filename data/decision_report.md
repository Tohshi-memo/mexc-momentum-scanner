# Decision Report

- generated_at: 2026-07-15T21:01:14.477451+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8764**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.75% / filled 20/20。**
- 全期間 MARKET基準: n=8764, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.75% | **+2.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.75% | **+2.75%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.66% | **+2.39%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.80% | **+2.10%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.26% | **+1.36%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.96% | **+1.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.14% | **+0.14%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.47% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 99件 (TP 34 / SL 63 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.89** / 初期 $100.00 (+242.89%)
- 確定: 2884件 (Win 903 / Loss 938 / Flat 1043) / skip 2441件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $342.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.40** / 初期 $100.00 (+5.40%)
- 確定: 728件 (Win 167 / Loss 168 / Flat 393) / skip 1447件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0942 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $105.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 174件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000240 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-15T21:01:08.163393+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64941.8
- Funnel: target 871 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +50.11% | $3,295,644.42 |
| SKL/USDT:USDT | +14.13% | $1,635,280.68 |
| CAP/USDT:USDT | +13.53% | $1,316,692.42 |
| HOME/USDT:USDT | +10.59% | $1,036,209.14 |
| SNXX/USDT:USDT | +10.23% | $1,323,655.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +2.35% | +2.34% |
| ALCH/USDT:USDT | below_1h_threshold | +1.36% | +1.35% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.76% | +0.75% |
| GRASS/USDT:USDT | below_1h_threshold | +0.56% | +0.56% |
| MYX/USDT:USDT | below_1h_threshold | +0.45% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
