# Decision Report

- generated_at: 2026-06-02T21:40:50.634049+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5490**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5490, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.22% | **-2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.27% | **+0.64%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.99% | **+0.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.20% | **+0.55%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.66% | **+0.30%** |
| LIMIT_10PCT | 2/20 | 10.0% | +1.81% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.12% | **+3.12%** |
| MARKET_LONG | 20/20 | 100.0% | +2.96% | **+2.96%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.68% | **+2.58%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +3.10% | **+2.32%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.77% | **+2.07%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1075件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T21:40:48.168231+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=67757.5
- Funnel: target 769 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +28.63% | $12,851,458.66 |
| LIT/USDT:USDT | +18.26% | $6,256,614.48 |
| ENA/USDT:USDT | +14.27% | $46,573,835.69 |
| GENIUS/USDT:USDT | +14.24% | $1,033,357.37 |
| BBSTOCK/USDT:USDT | +13.17% | $1,597,376.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BBSTOCK/USDT:USDT | below_1h_threshold | +3.52% | +3.22% |
| LIT/USDT:USDT | below_1h_threshold | +3.18% | +2.89% |
| ENA/USDT:USDT | below_1h_threshold | +3.02% | +2.72% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.68% | +2.38% |
| BSB/USDT:USDT | below_1h_threshold | +2.47% | +2.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
