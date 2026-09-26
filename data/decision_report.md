# Decision Report

- generated_at: 2026-09-26T17:41:41.346703+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15611**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=15611, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.99% | **+0.35%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.55% | **+0.28%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.32% | **+0.27%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.78% | **+1.34%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.21% | **+0.78%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.53% | **+0.61%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.60% | **+0.51%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.60% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,271.07** / 初期 $100.00 (+1171.07%)
- 確定: 5972件 (Win 1766 / Loss 1918 / Flat 2288) / skip 6200件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORDI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,271.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5489件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0832 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.84** / 初期 $100.00 (+19.84%)
- 確定: 3195件 (Win 941 / Loss 1266 / Flat 988) / pending 6件 / skip 3883件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000324 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ORDI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.84

## 6. Latest Market Context

- 更新: 2026-09-26T17:41:31.248941+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=84032.8
- Funnel: target 1070 → liquid 148 → pre 50 → checked 49 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=1
- Strict後reject: 4h RSI 66.2 >= 65=1, 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +9.78% | $1,036,866.79 |
| QNT/USDT:USDT | +6.69% | $15,029,024.32 |
| LSK/USDT:USDT | +4.77% | $2,518,877.49 |
| GALA/USDT:USDT | +3.62% | $2,630,151.22 |
| GRAM/USDT:USDT | +3.43% | $2,280,527.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RARE/USDT:USDT | below_1h_threshold | +4.67% | +4.72% |
| KAS/USDT:USDT | below_1h_threshold | +2.34% | +2.38% |
| LSK/USDT:USDT | below_1h_threshold | +1.61% | +1.66% |
| WLD/USDT:USDT | below_1h_threshold | +1.29% | +1.34% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.04% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
