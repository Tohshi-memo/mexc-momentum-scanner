# Decision Report

- generated_at: 2026-06-04T05:13:11.044998+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5604**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.81% / filled 20/20。**
- 全期間 MARKET基準: n=5604, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.81% | **+2.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.94% | **+2.94%** |
| MARKET | 20/20 | 100.0% | +2.81% | **+2.81%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.71% | **+1.37%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.86% | **-0.26%** |
| MARKET_LONG | 20/20 | 100.0% | -0.61% | **-0.61%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1160件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T05:13:08.318417+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.93% price=63768.6
- Funnel: target 771 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +25.28% | $25,236,478.71 |
| BP/USDT:USDT | +18.11% | $1,639,809.33 |
| EPIC/USDT:USDT | +15.10% | $3,995,172.38 |
| SIREN/USDT:USDT | +13.25% | $1,105,346.95 |
| STO/USDT:USDT | +12.92% | $7,233,632.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +1.22% | +2.15% |
| SIREN/USDT:USDT | below_1h_threshold | +0.73% | +1.67% |
| OPN/USDT:USDT | below_1h_threshold | +0.59% | +1.52% |
| OPG/USDT:USDT | below_1h_threshold | +0.46% | +1.39% |
| ZEC/USDT:USDT | below_1h_threshold | +0.42% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
