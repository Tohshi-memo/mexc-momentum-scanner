# Decision Report

- generated_at: 2026-07-20T12:01:16.292065+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9107**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9107, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.39% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +7.03% | **+5.27%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.69% | **+2.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.94% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$405.43** / 初期 $100.00 (+305.43%)
- 確定: 3169件 (Win 991 / Loss 1005 / Flat 1173) / skip 2499件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $405.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.12** / 初期 $100.00 (+27.12%)
- 確定: 1068件 (Win 278 / Loss 218 / Flat 572) / skip 1450件
- 成長率目線: 平均log +0.000225 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0669 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $127.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定: 306件 (Win 102 / Loss 135 / Flat 69) / pending 2件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.97

## 6. Latest Market Context

- 更新: 2026-07-20T12:01:09.714459+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64946.9
- Funnel: target 884 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +106.74% | $21,254,283.29 |
| BANK/USDT:USDT | +78.94% | $120,078,155.45 |
| EVAA/USDT:USDT | +26.31% | $7,067,929.56 |
| PROM/USDT:USDT | +23.87% | $3,668,577.57 |
| PUMPFUN/USDT:USDT | +15.57% | $34,600,421.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +3.13% | +3.17% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.52% | +1.56% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.49% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.49% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.40% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
