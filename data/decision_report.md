# Decision Report

- generated_at: 2026-05-12T16:08:27.618744+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4141**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=4141, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.33% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.53% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 277件 (Win 78 / Loss 96 / Flat 103) / skip 425件
- 成長率目線: 平均log +0.000593 / 幾何平均 +0.059% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUTH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $117.84

## 4. Latest Market Context

- 更新: 2026-05-12T16:08:24.244290+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80293.4
- Funnel: target 763 → liquid 195 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +4.10% | $1,315,692.04 |
| XNY/USDT:USDT | +3.67% | $1,313,459.40 |
| IRYS/USDT:USDT | +2.49% | $1,993,570.85 |
| ASTSSTOCK/USDT:USDT | +2.10% | $8,131,113.36 |
| JELLYJELLY/USDT:USDT | +1.74% | $1,186,668.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +4.11% | +4.12% |
| XNY/USDT:USDT | below_1h_threshold | +3.74% | +3.75% |
| IRYS/USDT:USDT | below_1h_threshold | +2.35% | +2.36% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +2.10% | +2.11% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +1.52% | +1.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
