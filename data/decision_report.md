# Decision Report

- generated_at: 2026-05-21T00:48:52.164829+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4587**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4587, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT | 8/20 | 40.0% | -1.03% | **-0.41%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.99% | **-0.44%** |
| LIMIT_7PCT | 7/20 | 35.0% | -1.31% | **-0.46%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.17% | **-0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +3.28% | **+2.87%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.39% | **+2.37%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.56% | **+1.28%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.95% | **+1.17%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.02** / 初期 $100.00 (+22.02%)
- 確定: 544件 (Win 138 / Loss 184 / Flat 222) / skip 604件
- 成長率目線: 平均log +0.000366 / 幾何平均 +0.037% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $122.02

## 4. Latest Market Context

- 更新: 2026-05-21T00:48:50.116608+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=77789.0
- Funnel: target 760 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +41.08% | $28,354,697.19 |
| NIL/USDT:USDT | +24.81% | $3,120,318.20 |
| FIDA/USDT:USDT | +17.22% | $11,771,327.68 |
| JTO/USDT:USDT | +14.34% | $2,875,935.40 |
| BEAT/USDT:USDT | +13.33% | $2,058,965.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.85% | +4.49% |
| NIL/USDT:USDT | below_1h_threshold | +4.49% | +4.13% |
| BSB/USDT:USDT | below_1h_threshold | +4.47% | +4.11% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.76% | +3.40% |
| BEAT/USDT:USDT | below_1h_threshold | +2.45% | +2.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
