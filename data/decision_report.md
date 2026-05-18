# Decision Report

- generated_at: 2026-05-18T03:23:39.403318+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4433**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=4433, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| ASK | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.17% | **+0.12%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.12% | **+0.08%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.03% | **+0.01%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.20% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.86** / 初期 $100.00 (+19.86%)
- 確定: 430件 (Win 111 / Loss 147 / Flat 172) / skip 564件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $119.86

## 4. Latest Market Context

- 更新: 2026-05-18T03:23:37.339976+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=76901.9
- Funnel: target 765 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +34.18% | $5,894,439.57 |
| AIGENSYN/USDT:USDT | +8.51% | $3,972,076.24 |
| HYPE/USDT:USDT | +3.70% | $304,877,286.94 |
| AKT/USDT:USDT | +3.61% | $1,504,245.67 |
| UB/USDT:USDT | +3.24% | $15,038,594.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +4.08% | +3.95% |
| FIDA/USDT:USDT | below_1h_threshold | +1.89% | +1.77% |
| KAS/USDT:USDT | below_1h_threshold | +0.44% | +0.32% |
| RUNE/USDT:USDT | below_1h_threshold | +0.34% | +0.21% |
| LDO/USDT:USDT | below_1h_threshold | +0.28% | +0.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
