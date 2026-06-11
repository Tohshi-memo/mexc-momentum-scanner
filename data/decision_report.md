# Decision Report

- generated_at: 2026-06-11T13:18:05.562262+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6354**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6354, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_BB3S | 6/18 | 33.3% | -0.09% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.03% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.67** / 初期 $100.00 (+49.67%)
- 確定: 1275件 (Win 322 / Loss 402 / Flat 551) / skip 1640件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.67

## 4. Latest Market Context

- 更新: 2026-06-11T13:18:02.440557+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62915.8
- Funnel: target 782 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +104.94% | $21,958,229.36 |
| VELVET/USDT:USDT | +73.34% | $82,912,883.24 |
| BEAT/USDT:USDT | +58.09% | $231,418,746.02 |
| AIO/USDT:USDT | +51.37% | $8,668,362.63 |
| COLLECT/USDT:USDT | +50.90% | $2,281,354.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.11% | +4.20% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.88% | +2.97% |
| STG/USDT:USDT | below_1h_threshold | +2.84% | +2.93% |
| AIO/USDT:USDT | below_1h_threshold | +2.69% | +2.78% |
| FIGHT/USDT:USDT | below_1h_threshold | +2.25% | +2.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
