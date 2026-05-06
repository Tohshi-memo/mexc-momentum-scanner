# Decision Report

- generated_at: 2026-05-06T18:37:40.476905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3492**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=3492, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.08% | **+0.92%** |
| LIMIT_BB3S | 6/15 | 40.0% | +1.87% | **+0.75%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.41% | **+2.05%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +3.17% | **+1.58%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.75% | **+1.37%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 44件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T18:37:35.071304+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=81279.1
- Funnel: target 766 → liquid 194 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +37.86% | $5,581,521.41 |
| TAG/USDT:USDT | +10.06% | $15,240,060.62 |
| FHE/USDT:USDT | +6.94% | $32,955,940.51 |
| TONCOIN/USDT:USDT | +5.14% | $245,864,216.93 |
| ZEREBRO/USDT:USDT | +5.09% | $1,050,776.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +3.32% | +3.47% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +2.35% | +2.50% |
| BILL/USDT:USDT | below_1h_threshold | +2.28% | +2.43% |
| JTO/USDT:USDT | below_1h_threshold | +1.79% | +1.94% |
| LYN/USDT:USDT | below_1h_threshold | +1.74% | +1.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
