# Decision Report

- generated_at: 2026-09-11T03:51:36.853603+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14196**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=14196, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.01% | **+0.00%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.06% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.78% | **+0.54%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.58% | **+0.46%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.32% | **+0.29%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,070.84** / 初期 $100.00 (+970.84%)
- 確定: 5368件 (Win 1615 / Loss 1735 / Flat 2018) / skip 5389件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,070.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.23** / 初期 $100.00 (+108.23%)
- 確定: 2790件 (Win 768 / Loss 650 / Flat 1372) / skip 4817件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0360 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.21** / 初期 $100.00 (+23.21%)
- 確定: 2700件 (Win 798 / Loss 1031 / Flat 871) / pending 5件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.21

## 6. Latest Market Context

- 更新: 2026-09-11T03:51:19.796883+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=76756.0
- Funnel: target 1066 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +51.92% | $8,481,988.29 |
| RAY/USDT:USDT | +23.39% | $8,175,015.79 |
| CNPY/USDT:USDT | +16.08% | $2,709,188.46 |
| PONS/USDT:USDT | +14.54% | $8,313,352.27 |
| MARSCOIN/USDT:USDT | +12.78% | $2,778,638.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HNT/USDT:USDT | below_1h_threshold | +3.69% | +3.76% |
| PONS/USDT:USDT | below_1h_threshold | +3.27% | +3.35% |
| XTZ/USDT:USDT | below_1h_threshold | +2.46% | +2.54% |
| ASTER/USDT:USDT | below_1h_threshold | +1.40% | +1.48% |
| BTR/USDT:USDT | below_1h_threshold | +1.14% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
