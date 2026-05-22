# Decision Report

- generated_at: 2026-05-22T19:44:03.368280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4736**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4736, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +4.29% | **+1.29%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.29% | **+0.64%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.98% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.06% | **+2.03%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +4.60% | **+1.84%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.06** / 初期 $100.00 (+25.06%)
- 確定: 582件 (Win 149 / Loss 188 / Flat 245) / skip 715件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $125.06

## 4. Latest Market Context

- 更新: 2026-05-22T19:44:01.235674+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.04% price=75706.2
- Funnel: target 765 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +68.37% | $36,841,707.39 |
| BILL/USDT:USDT | +9.23% | $14,570,466.81 |
| BEAT/USDT:USDT | +8.75% | $37,011,064.06 |
| BUILDONBOB/USDT:USDT | +4.93% | $5,950,025.70 |
| LAB/USDT:USDT | +4.32% | $28,012,772.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +4.85% | +5.88% |
| LAB/USDT:USDT | below_1h_threshold | +4.18% | +5.21% |
| GUA/USDT:USDT | below_1h_threshold | +3.72% | +4.75% |
| BSB/USDT:USDT | below_1h_threshold | +3.47% | +4.51% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.40% | +2.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
