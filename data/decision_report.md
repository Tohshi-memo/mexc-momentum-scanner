# Decision Report

- generated_at: 2026-06-04T02:15:26.082309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5592**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.11% / filled 20/20。**
- 全期間 MARKET基準: n=5592, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+4.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.11% | **+4.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +4.13% | **+4.13%** |
| MARKET | 20/20 | 100.0% | +4.11% | **+4.11%** |
| LIMIT_1PCT | 17/20 | 85.0% | +4.03% | **+3.42%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.51% | **+2.11%** |
| LIMIT_3PCT | 10/20 | 50.0% | +3.77% | **+1.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +0.69% | **+0.34%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.63% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1148件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T02:15:23.740196+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=62355.8
- Funnel: target 771 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +29.42% | $23,116,636.29 |
| STO/USDT:USDT | +12.02% | $6,936,496.96 |
| MAGMA/USDT:USDT | +8.66% | $4,401,802.76 |
| SKYAI/USDT:USDT | +4.79% | $15,398,205.25 |
| BP/USDT:USDT | +4.51% | $1,571,614.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_relative_strength | +5.16% | +4.81% |
| OPN/USDT:USDT | below_1h_threshold | +4.43% | +4.09% |
| US/USDT:USDT | below_1h_threshold | +2.68% | +2.33% |
| BEAT/USDT:USDT | below_1h_threshold | +1.39% | +1.04% |
| BILL/USDT:USDT | below_1h_threshold | +1.28% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
