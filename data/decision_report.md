# Decision Report

- generated_at: 2026-05-18T04:03:34.032503+00:00
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

- 更新: 2026-05-18T04:03:32.053032+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76932.3
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +24.71% | $5,952,962.37 |
| AIGENSYN/USDT:USDT | +12.61% | $3,966,542.75 |
| HYPE/USDT:USDT | +4.37% | $288,672,499.15 |
| ZEC/USDT:USDT | +4.06% | $490,087,508.36 |
| AKT/USDT:USDT | +3.93% | $1,465,443.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.80% | +1.76% |
| OPENLEDGER/USDT:USDT | below_1h_threshold | +1.18% | +1.13% |
| BILL/USDT:USDT | below_1h_threshold | +1.17% | +1.13% |
| ZEC/USDT:USDT | below_1h_threshold | +1.12% | +1.08% |
| BEAT/USDT:USDT | below_1h_threshold | +0.70% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
