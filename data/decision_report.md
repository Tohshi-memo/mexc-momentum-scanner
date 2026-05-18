# Decision Report

- generated_at: 2026-05-18T11:53:07.985443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4441**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4441, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.22% | **+0.21%** |
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.11% | **+0.04%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.69% | **+1.69%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.52% | **+0.31%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.30% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$95.74** / 初期 $100.00 (-4.26%)
- 確定トレード: 53件 (TP 13 / SL 37 / EXP 3)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.02** / 初期 $100.00 (+22.02%)
- 確定: 438件 (Win 114 / Loss 148 / Flat 176) / skip 564件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.02

## 4. Latest Market Context

- 更新: 2026-05-18T11:53:06.426561+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=77179.1
- Funnel: target 768 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=2, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRAC/USDT:USDT | +49.51% | $1,060,638.72 |
| FIDA/USDT:USDT | +44.32% | $9,310,874.37 |
| BSB/USDT:USDT | +15.19% | $19,113,409.32 |
| OPENLEDGER/USDT:USDT | +12.60% | $1,431,447.04 |
| RIVER/USDT:USDT | +6.04% | $9,766,814.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_relative_strength | +5.18% | +4.60% |
| SPACE/USDT:USDT | below_relative_strength | +5.15% | +4.56% |
| OPENLEDGER/USDT:USDT | below_1h_threshold | +3.07% | +2.49% |
| EDU/USDT:USDT | below_1h_threshold | +2.17% | +1.59% |
| GUA/USDT:USDT | below_1h_threshold | +2.15% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
