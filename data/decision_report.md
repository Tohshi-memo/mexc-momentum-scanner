# Decision Report

- generated_at: 2026-05-17T15:08:23.772048+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4407**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4407, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.73% | **+0.17%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.19% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.87% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +1.26% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 404件 (Win 104 / Loss 137 / Flat 163) / skip 564件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $119.41

## 4. Latest Market Context

- 更新: 2026-05-17T15:08:21.789960+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78061.4
- Funnel: target 760 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +64.56% | $2,373,354.59 |
| BSB/USDT:USDT | +48.50% | $17,216,902.27 |
| AIA/USDT:USDT | +46.67% | $19,025,136.76 |
| DUSK/USDT:USDT | +18.08% | $1,159,496.99 |
| CGPT/USDT:USDT | +17.70% | $2,407,055.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.99% | +2.92% |
| UP/USDT:USDT | below_1h_threshold | +1.04% | +0.97% |
| CGPT/USDT:USDT | below_1h_threshold | +0.69% | +0.62% |
| APE/USDT:USDT | below_1h_threshold | +0.59% | +0.52% |
| BEAT/USDT:USDT | below_1h_threshold | +0.55% | +0.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
