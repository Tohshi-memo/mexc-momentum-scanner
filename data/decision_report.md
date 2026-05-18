# Decision Report

- generated_at: 2026-05-18T02:48:51.656926+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4432**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=4432, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| ASK | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.91% | **+0.64%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.84% | **+0.59%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.44%** |
| ASK_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.46** / 初期 $100.00 (+20.46%)
- 確定: 429件 (Win 111 / Loss 146 / Flat 172) / skip 564件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.46

## 4. Latest Market Context

- 更新: 2026-05-18T02:48:49.539825+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=76879.1
- Funnel: target 765 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +30.41% | $5,741,503.99 |
| AIGENSYN/USDT:USDT | +15.52% | $3,640,734.90 |
| HYPE/USDT:USDT | +5.45% | $307,303,892.70 |
| AKT/USDT:USDT | +5.23% | $1,433,351.14 |
| LYN/USDT:USDT | +3.94% | $2,490,564.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.35% | +2.61% |
| SIREN/USDT:USDT | below_1h_threshold | +2.23% | +2.50% |
| AKT/USDT:USDT | below_1h_threshold | +1.79% | +2.05% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.59% | +1.85% |
| H/USDT:USDT | below_1h_threshold | +1.48% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
