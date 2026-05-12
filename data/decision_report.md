# Decision Report

- generated_at: 2026-05-12T02:32:47.713135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4090**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4090, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.26% | **+0.85%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.70% | **+0.59%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.05% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.89** / 初期 $100.00 (+10.89%)
- 確定: 227件 (Win 59 / Loss 79 / Flat 89) / skip 424件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $110.89

## 4. Latest Market Context

- 更新: 2026-05-12T02:32:42.506196+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81177.6
- Funnel: target 762 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +47.85% | $1,819,782.85 |
| SKYAI/USDT:USDT | +37.19% | $39,290,082.01 |
| USELESS/USDT:USDT | +20.73% | $4,296,646.13 |
| H/USDT:USDT | +15.55% | $16,269,016.52 |
| GUA/USDT:USDT | +14.25% | $1,074,254.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +3.39% | +3.35% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.43% | +2.39% |
| ONDO/USDT:USDT | below_1h_threshold | +2.42% | +2.39% |
| VVV/USDT:USDT | below_1h_threshold | +2.32% | +2.29% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +2.25% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
