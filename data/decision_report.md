# Decision Report

- generated_at: 2026-06-02T23:16:27.192352+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5499**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5499, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.67% | **+0.47%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.41% | **+0.24%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.06% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| ASK_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +1.10% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.86% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1083件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T23:16:24.711281+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.54% price=66713.7
- Funnel: target 770 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +34.81% | $12,755,131.98 |
| US/USDT:USDT | +27.08% | $7,328,156.03 |
| LIT/USDT:USDT | +18.54% | $6,620,170.25 |
| MRVLSTOCK/USDT:USDT | +14.19% | $15,258,712.10 |
| BBSTOCK/USDT:USDT | +14.08% | $1,755,172.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.40% | +3.86% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.40% | +1.86% |
| LIT/USDT:USDT | below_1h_threshold | +1.71% | +1.17% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.34% | +0.80% |
| SPX/USDT:USDT | below_1h_threshold | +1.23% | +0.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
