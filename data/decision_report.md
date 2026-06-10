# Decision Report

- generated_at: 2026-06-10T17:56:37.039128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6236**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6236, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.37% | **-1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.01% | **+1.31%** |
| ASK_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.98%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.00** / 初期 $100.00 (+49.00%)
- 確定: 1229件 (Win 306 / Loss 384 / Flat 539) / skip 1568件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.00

## 4. Latest Market Context

- 更新: 2026-06-10T17:56:34.229282+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=61883.7
- Funnel: target 785 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FOLKS/USDT:USDT | +12.63% | $5,083,019.62 |
| BTW/USDT:USDT | +6.66% | $33,802,530.36 |
| VELVET/USDT:USDT | +6.38% | $15,871,882.11 |
| STRAX/USDT:USDT | +5.39% | $1,128,832.31 |
| BLESS/USDT:USDT | +4.11% | $2,817,214.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRAX/USDT:USDT | below_1h_threshold | +4.86% | +5.35% |
| BSB/USDT:USDT | below_1h_threshold | +4.81% | +5.31% |
| BTW/USDT:USDT | below_1h_threshold | +3.33% | +3.82% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +2.29% |
| POWER/USDT:USDT | below_1h_threshold | +1.68% | +2.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
